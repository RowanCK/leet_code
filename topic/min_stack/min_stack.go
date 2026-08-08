package min_stack

type MinStack struct {
	stack    []int
	minStack []int
}

func Constructor() MinStack {
	return MinStack{
		stack:    []int{},
		minStack: []int{},
	}
}

func (this *MinStack) Push(value int) {
	this.stack = append(this.stack, value)
	if len(this.minStack) == 0 || value <= this.minStack[len(this.minStack)-1] {
		this.minStack = append(this.minStack, value)
	}
}

func (this *MinStack) Pop() {
	if len(this.stack) == 0 {
		return
	}

	top := this.stack[len(this.stack)-1]

	if top == this.minStack[len(this.minStack)-1] {
		this.minStack = this.minStack[:len(this.minStack)-1]
	}

	this.stack = this.stack[:len(this.stack)-1]
}

func (this *MinStack) Top() int {
	if len(this.stack) > 0 {
		return this.stack[len(this.stack)-1]
	}
	return 0
}

func (this *MinStack) GetMin() int {
	if len(this.minStack) > 0 {
		return this.minStack[len(this.minStack)-1]
	}
	return 0
}

func MinStackFunc() {
	minStack := MinStack{}

	minStack.Push(-2)
	minStack.Push(0)
	minStack.Push(-3)
	minStack.GetMin() // -3

	minStack.Pop()
	minStack.Top()    // 0
	minStack.GetMin() // -2
}
