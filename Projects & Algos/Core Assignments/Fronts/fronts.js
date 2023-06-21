class Node {
    constructor(value) {
    this.value = value;
    this.next = null;
    }
}

class SLL {
    constructor() {
    this.head = null;
    }

    front() {
    if (this.head === null) {
        return null;
    }
    return this.head.value;
    }

    addFront(value) {
    let newNode = {
        value: value,
        next: this.head
    };
    this.head = newNode;
    }

    removeFront() {
    if (this.head === null) {
        return null;
    }
    let removedNode = this.head;
    this.head = this.head.next;
    removedNode.next = null;
    return removedNode.value;
    }

    addBack(value) {
    let newNode = new Node(value);

    if (this.head === null) {
        this.head = newNode;
    } else {
        let currentNode = this.head;
        while (currentNode.next !== null) {
        currentNode = currentNode.next;
        }
        currentNode.next = newNode;
    }
    }
}

let myList = new SLL();
myList.addBack(1);
myList.removeFront(2);
myList.addBack(3);
console.log(myList.head);



