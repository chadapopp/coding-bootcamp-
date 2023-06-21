class Node{
    constructor(value){
        this.value = value;
        this.next = null;
    }
}

class SLL{
    constructor(){
        this.head = null
    }

    addFront(value){
        let newNode = new Node(value);
        newNode.next = this.head;
        this.head = newNode
    }

    contains(value){
        let currentNode = this.head;
        while(currentNode !== null){
            if (currentNode.value === value){
                return true;
            }
            currentNode = currentNode.next;
        }
        return false;
    }

    length(){
        let count = 0;
        let currentNode = this.head;
        while (currentNode !== null){
            count++;
            currentNode = currentNode.next;
        }
        return count;
    }

    display(){
        let str = "";
        let currentNode = this.head;
        while (currentNode !== null){
            str += currentNode.value + " ";
            currentNode = currentNode.next;
        }
        return str.trim();
    }
}

let myList = new SLL();
myList.addFront(1);
myList.addFront(2);
myList.addFront(3);
console.log(myList.contains(2));


