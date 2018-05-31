package BlockUtils

import (
	"crypto/sha256"
	"encoding/hex"
	"time"
	"bytes"
	"log"
	"github.com/adam-hanna/randomstrings"
	"../BlockElement"
)

// Purpose : Returns SHA256 hash of a string
func CalculateHash(s string) string {
	h := sha256.New()
	h.Write([]byte(s))
	hashed := h.Sum(nil)
	return hex.EncodeToString(hashed)
}

// Purpose : Returns SHA256 hash of a Block
func CalculateBlockHash(block BlockElement.Block) string {
	record := string(block.Index) + block.Timestamp + string(block.NodeData) + block.PrevHash
	return CalculateHash(record)
}

// Purpose : Accepts Previous Block and new Block data to make a new block
func GenerateBlock(oldBlock BlockElement.Block, NodeData int, address string) (BlockElement.Block, error) {

	var newBlock BlockElement.Block
	t := time.Now()
	newBlock.Index = oldBlock.Index + 1
	newBlock.Timestamp = t.String()
	newBlock.NodeData = NodeData
	newBlock.PrevHash = oldBlock.Hash
	newBlock.Hash = CalculateBlockHash(newBlock)
	newBlock.Validator = address

	return newBlock, nil
}

// Purpose : Accepts Previous Block and new Block data and return true or false based on conditional validity
func IsBlockValid(newBlock, oldBlock BlockElement.Block) bool {
	if oldBlock.Index+1 != newBlock.Index {
		return false
	}
	if oldBlock.Hash != newBlock.PrevHash {
		return false
	}
	if CalculateBlockHash(newBlock) != newBlock.Hash {
		return false
	}
	return true
}

func AssignAddressToNode() string{
	var buffer bytes.Buffer
	buffer.WriteString("USER_")
	sRand, err := randomstrings.GenerateRandomString(6)
	buffer.WriteString(sRand)
	address := buffer.String()
	if err != nil {
		// panic!
	}
	log.Println(sRand)
	//r := rand.New(rand.NewSource(99))
	//address := s + strconv.Itoa(r.Perm(10)) + strconv.Itoa(r.Perm(222))
	return address
}

func PrettyPrintBlock() {
}


