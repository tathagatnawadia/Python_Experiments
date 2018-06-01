package main

// import "Hotels"

import (
	"bufio"
	"encoding/json"
	"fmt"
	"github.com/davecgh/go-spew/spew"
	"github.com/joho/godotenv"
	"io"
	"log"
	"math/rand"
	"net"
	"os"
	"strconv"
	"sync"
	"time"
)

import (
	"./BlockElement"
	"./BlockUtils"
)

type BC struct {
	// Purpose : the main immutable blockchain
	Blockchain []BlockElement.Block
	// Purpose : 
	TempBlocks []BlockElement.Block
	// Purpose : Handles incoming blocks for validation
	CandidateBlocks chan BlockElement.Block
	// Purpose : Winning announcement channel for all the nodes
	Announcements chan string
	// Purpose : Holds the stake of each node
	Validators map[string]int
	// Purpose : Marks whether the genesis block is made for the chain
	Genesis bool
	// Purpose : 
	WinningInterval int
}

var ethereum = BC{nil,nil, make(chan BlockElement.Block), make(chan string), make(map[string]int), false, 13}
var mutex = &sync.Mutex{}


// Purpose : Handles each connection
func handleNode(conn net.Conn) {
	defer conn.Close()

	/*
	------------------------------------------------------
	Purpose : Announce the winner nodes for every cycle to each of the node connections
	------------------------------------------------------
	*/
	go func() {
		for {
			msg := <-ethereum.Announcements
			io.WriteString(conn, msg)
		}
	}()

	/*
	------------------------------------------------------
	Purpose : Ask the number of committed tokens for every node connection
	------------------------------------------------------
	*/

	var address string

	io.WriteString(conn, "Enter token balance:")
	scanBalance := bufio.NewScanner(conn)
	for scanBalance.Scan() {
		balance, err := strconv.Atoi(scanBalance.Text())
		if err != nil {
			log.Printf("%v not a number: %v", scanBalance.Text(), err)
			return
		}
		address = BlockUtils.AssignAddressToNode()
		// TODO : Add logic so that nodes cannot add more than 49% of the total node network
		// TODO : Profiling of the users
		ethereum.Validators[address] = balance
		fmt.Println(ethereum.Validators)
		io.WriteString(conn, address)
		break
	}

	/*
	------------------------------------------------------
	Purpose : Ask the node if it want to propose data to the blockchain
	------------------------------------------------------
	*/

	io.WriteString(conn, "\nEnter a new NODEDATA:")
	scanNodeData := bufio.NewScanner(conn)

	go func() {
		for {

			// Read the scanned data and scan again
			for scanNodeData.Scan() {
				nodedata, err := strconv.Atoi(scanNodeData.Text())
				// If input != Integer the error and address is deleted from the validators list and they lose their staked tokens
				if err != nil {
					log.Printf("%v is corrupted%v", scanNodeData.Text(), err)
					delete(ethereum.Validators, address)
					conn.Close()
				}

				mutex.Lock()
				oldLastIndex := ethereum.Blockchain[len(ethereum.Blockchain)-1]
				mutex.Unlock()

				// create newBlock for consideration to be forged
				newBlock, err := BlockUtils.GenerateBlock(oldLastIndex, nodedata, address)
				if err != nil {
					log.Println(err)
					continue
				}

				// check if the block is valid and add it to Candidate Blocks
				if BlockUtils.IsBlockValid(newBlock, oldLastIndex) {
					ethereum.CandidateBlocks <- newBlock
				}
				io.WriteString(conn, "\nEnter a new NODEDATA:")
			}
		}
	}()

	/*
	------------------------------------------------------
	Purpose : Minute Intervaled broadcast to all the nodes about the blockchain
	------------------------------------------------------
	*/
	for {
		time.Sleep(time.Minute)
		mutex.Lock()
		output, err := json.Marshal(ethereum.Blockchain)
		mutex.Unlock()
		if err != nil {
			log.Fatal(err)
		}
		io.WriteString(conn, string(output)+"\n")
	}

}

// Purpose : Handles the pickWinner
func pickWinningValidator() {
	time.Sleep(time.Duration(ethereum.WinningInterval) * time.Second)
	/*
	------------------------------------------------------
	Purpose : temp contains all the blocks proposed during the interval
	------------------------------------------------------
	*/
	mutex.Lock()
	temp := ethereum.TempBlocks
	mutex.Unlock()


	lotteryPool := []string{} // Holds the array of node address in multiple of stakes they have put
	if len(temp) > 0 { // If the number of proposed blocks during that time != 0 

		SKIP_NODE:
		/*
		------------------------------------------------------
		Purpose : Prepare LotteryPool Iterate through each block proposed in this timeinterval
		------------------------------------------------------
		*/
		for _, block := range temp {
			// Skip the 
			for _, node := range lotteryPool {
				if block.Validator == node {
					continue SKIP_NODE
				}
			}

			// Lock validators
			mutex.Lock()
			setValidators := ethereum.Validators
			mutex.Unlock()

			numberOfStakes, validatorOk := setValidators[block.Validator]
			if validatorOk { // If the node address is registered as  
				for i := 0; i < numberOfStakes; i++ { // Iterate as many times as number of stakes
					lotteryPool = append(lotteryPool, block.Validator)
				}
			}
		}

		/*
		------------------------------------------------------
		Purpose : Choose winner from LotteryPool
		------------------------------------------------------
		*/
		s := rand.NewSource(time.Now().Unix())
		r := rand.New(s)
		lotteryWinner := lotteryPool[r.Intn(len(lotteryPool))]

		/*
		------------------------------------------------------
		Purpose : Add the winner's blocks to the block chain
		------------------------------------------------------
		*/
		for _, block := range temp {
			if block.Validator == lotteryWinner {
				mutex.Lock()
				ethereum.Blockchain = append(ethereum.Blockchain, block)
				mutex.Unlock()
			}
		}
		/*
		------------------------------------------------------
		Purpose : Announce winner to all the nodes on the network
		------------------------------------------------------
		*/
		for _ = range ethereum.Validators {
			ethereum.Announcements <- "\nWinning node : " + lotteryWinner + "\n"
		}
	}

	mutex.Lock()
	ethereum.TempBlocks = []BlockElement.Block{}
	mutex.Unlock()
}

func generateGenesisBlock() BlockElement.Block {
	timestamp := time.Now()
	genesisBlock := BlockElement.Block{}
	genesisBlock = BlockElement.Block{0, timestamp.String(), 0, BlockUtils.CalculateBlockHash(genesisBlock), "", "Genesis Block"}
	spew.Dump(genesisBlock)
	return genesisBlock
}

func main() {

	err := godotenv.Load()
	if err != nil {
		log.Fatal(err)
	}

	/*
	------------------------------------------------------
	Purpose : Create Genesis block and add it to the blockchain
	------------------------------------------------------
	*/
	genesisBlock := generateGenesisBlock()
	ethereum.Blockchain = append(ethereum.Blockchain, genesisBlock)

	/*
	------------------------------------------------------
	Purpose : Open a tcp connection for nodes to join via nc
	------------------------------------------------------
	*/
	server, err := net.Listen("tcp", ":"+os.Getenv("ADDR"))
	if err != nil {
		log.Fatal(err)
	}
	defer server.Close()

	/*
	------------------------------------------------------
	Purpose : Add the blocks coming in via nodes from the channel CandidateBlocks to TempBlock for pickWinningValidator
	------------------------------------------------------
	*/
	go func() {
		for candidate := range ethereum.CandidateBlocks {
			mutex.Lock()
			ethereum.TempBlocks = append(ethereum.TempBlocks, candidate)
			mutex.Unlock()
		}
	}()


	/*
	------------------------------------------------------
	Purpose : Decide the winner from the tempBlocks and then empty it
	------------------------------------------------------
	*/
	go func() {
		for {
			pickWinningValidator()
		}
	}()

	/*
	------------------------------------------------------
	Purpose : Handler for each node connection which joins the network
	------------------------------------------------------
	*/
	for {
		conn, err := server.Accept()
		if err != nil {
			log.Fatal(err)
		}
		go handleNode(conn)
	}
}
