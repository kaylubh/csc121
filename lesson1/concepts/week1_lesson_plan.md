# 🐍 Lesson Plan: Introduction to Python Programming Fundamentals

* **Course:** Introduction to Python (e.g., CSC 121)
* **Lesson Title:** Getting Started with Python: Projects, Variables, Input, Calculations, and Output
* **Tools:** PyCharm (Community or Edu), Python 3.x

---

# 🧩 Part 1: What is a Program?

* A program = instructions for the computer
* Most programs follow:

> Input → Processing → Output

Examples:

* Calculator
* Grade average
* Game score tracker

Before learning any programming language, it’s important to understand **how programs work conceptually**.

Almost **every program in the world** follows this pattern:

> **Input → Processing → Output**

---

## 🌎 Examples from Real Life

* A calculator:

  * Input: numbers
  * Processing: math
  * Output: answer

* A game:

  * Input: keyboard or controller
  * Processing: game rules and logic
  * Output: graphics and sound

* A grade calculator:

  * Input: scores
  * Processing: average calculation
  * Output: final grade

---

# 📥 1. Input — Getting Data Into the Program

## 💡 What Is Input?

**Input** is any data the program receives from the outside world.

Input can come from:

* The keyboard
* A file
* A button click
* The internet
* Another program

---

### Examples of Input:

* A name
* A number
* A temperature
* A price
* A yes/no answer

> Input answers the question:
> **“What information does the program need to do its job?”**

---

# 📦 2. Variables — Remembering Information

## 💡 What Is a Variable?

A **variable** is:

> A **name we give to a place in the computer’s memory** where a value is stored.

---

## 🧠 What’s Really Happening Behind the Scenes?

When you create a variable, the computer:

1. Finds a **location in memory**
2. Stores a **value** there
3. Lets you use a **name** to refer to that location

So:

> The **computer uses memory addresses**.
> **Humans use variable names.**

---

## 🏠 Real-Life Analogy: Labeled Boxes in a Warehouse

Imagine a huge warehouse (the computer’s memory) with millions of boxes.

Each box:

* Has an **address**
* Holds **one thing**

Instead of saying:

> “Go to box A839201”

We put a **label** on the box:

> “PRICE”

So:

* The **label** = variable name
* The **box** = memory location
* The **thing inside** = value

---

## 🧪 Conceptual Example

If a program asks for your name and you type:

> Alex

The computer:

* Stores `"Alex"` in memory somewhere
* Attaches the name: `user_name` to that location

So conceptually:

> `user_name` → (memory location) → `"Alex"`

Later, when the program uses `user_name`, it:

* Goes to that memory location
* Gets `"Alex"`

---

## 🧮 Another Example: Calculation

If:

* hours = 5
* rate = 20
* pay = hours × rate

Then in memory:

* One location holds `5`
* One holds `20`
* One holds `100`

And the names:

* `hours`
* `rate`
* `pay`

…are just **labels** for those memory locations.

---

## 🔁 Changing a Variable

If you do:

* > total = 50
* > total = 75

You did **not** create a new box.

You **replaced the value inside the same box**.

---

## 🧑‍🎓 The Simple Truth

> Variables are **named memory locations**.

---

# ⚙️ 3. Processing — Doing Work With the Data

## 💡 What Is Processing?

**Processing** is:

> The part of the program where **thinking, calculating, and decision-making happens**.

Processing includes:

* Math calculations
* Comparing values
* Applying rules
* Making decisions
* Combining text

---

### Examples:

* Calculate tax
* Compute an average
* Convert temperature
* Decide pass/fail
* Compute total pay

> Processing answers:
> **“What should the program DO with the input?”**

---

# 🔤 Strings vs 🔢 Numbers (Two Very Different Kinds of Data)

When a program stores information in variables, that information can be **different types**.

Two of the most important types are:

* > 🅰️ **Strings** (text)
* > 🅱️ **Numbers** (values you can do math with)

---

## 🅰️ What Is a String?

A **string** is:

> **Text** — words, names, sentences, or anything made of characters.

Examples of strings:

* `"Alex"`
* `"Hello"`
* `"123 Main Street"`
* `"CS101"`
* `"5"`  ← looks like a number, but it is **text**

---

### What Are Strings Used For?

Strings are used for:

* Names
* Messages
* Labels
* Sentences
* Anything meant to be **read**, not calculated

---

### Important Rule About Strings

> You **do not do math** with strings.

You can:

* Display them
* Combine them with other text
* Store them
* Show them to the user

But you **cannot**:

* Add them like numbers
* Multiply them like numbers
* Use them in formulas

---

## 🅱️ What Is a Number?

A **number** is:

> A value the computer can **use in calculations**.

Examples of numbers:

* `5`
* `10`
* `3.14`
* `-2`
* `100`

Numbers can represent:

* Counts
* Prices
* Scores
* Measurements
* Totals

---

### What Are Numbers Used For?

Numbers are used for:

* Adding
* Subtracting
* Multiplying
* Dividing
* Comparing
* Calculating results

---

## ⚠️ The Super Common Beginner Mistake

> Confusing `"5"` with `5`

They look similar, but:

* `"5"` = a **string** (text)
* `5` = a **number** (math value)

---

### Real-Life Analogy

Think of:

* `"5"` as the **word** “five” written on paper
* `5` as **five actual objects**

You can’t:

* Add the word “five” to another word and get math
  But you can:
* Add five apples to five apples and get ten apples 🍎🍎🍎🍎🍎🍎🍎🍎🍎🍎

---

## 🧠 Why This Matters in Programs

Many programs:

1. Get input from the user
2. The input **starts as text**
3. If you want to do math, you must **treat it as a number**

So conceptually:

> Input → (text) → convert to number → do math → output

---

## 🧪 Conceptual Example (No Code)

If the user types:

> 5

The computer first sees:

> `"5"` (a string)

If you want to:

* Add
* Multiply
* Calculate

You must:

> Convert `"5"` into the number `5`

---

## 🧱 Summary Table

| Concept          | String                  | Number       |
| ---------------- | ----------------------- | ------------ |
| What it is       | Text                    | A math value |
| Used for         | Names, messages, labels | Calculations |
| Can do math?     | ❌ No                    | ✅ Yes        |
| Example          | `"25"`                  | `25`         |
| Stored in memory | ✅ Yes                   | ✅ Yes        |

---

## 🧑‍🎓 The One-Sentence Rule

> If it’s meant to be **read**, it’s probably a **string**.
> If it’s meant to be **calculated**, it must be a **number**.

---

## ⚠️ Another Common Mistake

> A program crashes or gives weird results because the student tries to do math with text.

This is **normal** when learning — and now you know why it happens.

---

## 🧠 How This Connects to Variables

Variables don’t just store values — they store **types of values**:

* Some variables store **strings**
* Some variables store **numbers**

And the program must use them **correctly**.

---

# 🧾 What Is an Assignment Statement?

An **assignment statement** is:

> An instruction that **stores a value into a variable** (a named memory location).

In plain English:

> It **puts something into a box** and puts a **label on that box**.

---

## 🧠 What Actually Happens

When a program executes an assignment statement, the computer:

1. Finds a **location in memory**
2. Puts a **value** there
3. Associates that location with a **name**

So conceptually:

> Variable name = memory location holding a value

---

## 🏷️ Real-Life Analogy

Think of a warehouse with empty boxes.

If you say:

> “Put 20 in the box labeled HOURS”

You just **assigned** the value `20` to the box called `HOURS`.

Later, if you say:

> “Put 25 in the box labeled HOURS”

You did **not** make a new box.

You:

> Replaced the value in the same box.

---

## 🧪 Conceptual Examples (Not Language-Specific)

When you see something like:

> total = 100

It means:

> “Store the value 100 in the memory location named `total`.”

---

If you see:

> pay = hours × rate

It means:

> “Calculate hours × rate, then store the result in `pay`.”

So:

> The **right side is processed first**, then the **result is stored** in the variable on the left.

---

## ⚠️ Very Important Rule

> An assignment statement is **not** a math equation.

It does **not** mean:

> “total equals 100 forever”

It means:

> “Take 100 and store it in `total` right now.”

---

## 🔁 Variables Can Be Reassigned

You can assign a new value to the same variable later:

* > total = 50
* > total = 75

This means:

> The value in `total` changed from 50 to 75.

The **box is the same** — only the **contents changed**.

---

## 🧠 Assignment + Processing Together

Many assignments include **processing**:

> average = (score1 + score2 + score3) / 3

Conceptually:

1. Add the three scores
2. Divide by 3
3. Store the result in `average`

---

## 🧱 Assignment Is How Programs Remember Things

Without assignment statements:

* The program couldn’t store input
* The program couldn’t store results
* The program would forget everything immediately

So:

> Assignment statements are how programs **remember information**.

---

## 🔤 Assignment Works With All Types of Data

You can assign:

* Strings (text)
* Numbers
* Results of calculations
* Results of decisions

Examples (conceptually):

* name = "Alex" → store text
* age = 20 → store number
* total = price + tax → store calculation result

---

## 🧑‍🎓 The One-Sentence Definition

> An assignment statement **stores a value into a variable** (a named memory location).

---

## 🧠 Even Simpler

> Assignment = **put this value into that variable**.

---

## ⚠️ Super Common Beginner Confusion

Beginners often think:

> `x = x + 1` makes no sense in math.

In programming it means:

> “Take the current value of `x`, add 1 to it, and store the result back into `x`.”

---

## 🎯 Why This Concept Is So Important

Because:

* Input is stored using assignment
* Calculations are stored using assignment
* Results are stored using assignment
* Variables only exist because of assignment

> Assignment is the **glue** that connects memory, variables, and processing.

---

# 📤 4. Output — Showing Results

## 💡 What Is Output?

**Output** is:

> The information the program sends **back to the user**.

Output can be:

* Text on a screen
* A file
* A message
* A chart
* A sound

---

### Examples:

* “Your total is $23.45”
* “You passed!”
* “Your average is 82”

> Output answers:
> **“What result should the user see?”**

---

# 📝 5. Comments — Explaining the Program

## 💡 What Are Comments?

**Comments** are:

> Notes written **for humans**, not for the computer.

The computer **ignores them**.

---

### Why We Use Comments

* Explain what the program does
* Explain why something is done
* Make code easier to read
* Help your future self
* Help teammates and instructors

> Comments are like **notes in the margin of a textbook**.

---

# 🧩 The Program Recipe (Almost Always)

1. Get input
2. Store it in variables
3. Process it
4. Store results in variables
5. Show output

---

# 🏗️ Example (In Plain English)

### Pay Calculator:

* Input: hours worked, hourly rate
* Variables: hours, rate, pay
* Processing: hours × rate
* Output: total pay

---

# ⚠️ Important: How *Not* to Use Variables

## 🧙‍♂️ Magic Numbers

A **magic number** is:

> A number in a program whose meaning is **not obvious**.

Example:

> Why is `32` used? Why `100`? Why `0.08`?

Instead:

> Important numbers should be stored in **named variables** so humans understand them.

---

## 🧱 Hardcoding

**Hardcoding** means:

> Writing values directly into the program instead of using variables or input.

Bad examples:

* A pay program that always uses $15/hour
* A tax program that always uses 7%
* A grade program that always assumes 100 points

---

### Why This Is Bad

* ❌ The program only works in one situation
* ❌ You must edit the code to change values
* ❌ The program is fragile and unprofessional

---

## ✅ Better Idea

> If a value might change or has real-world meaning, **store it in a variable or get it as input**.

---

## 🏷️ How to Name Variables

Good variable names:

* Describe what is stored
* Are clear and readable

### ✅ Good Names:

* `price`
* `tax_rate`
* `hours_worked`
* `total_score`

### ❌ Bad Names:

* `x`
* `n1`
* `thing`
* `temp2`

---

## 🧠 The Naming Test

If this sounds good:

> “The variable `tax_rate` stores the tax rate.”

Good name.

If this sounds bad:

> “The variable `x7` stores the x7.”

Bad name.

---

## 🧱 One More Good Habit

> Put important values in **one place** at the top of the program.

So they’re easy to:

* Find
* Change
* Verify

---

# 🧨 The #1 Beginner Mistake

> Writing code without planning.

Always ask first (IPO):

1. What inputs do I need?
2. What variables do I need?
3. What processing do I need?
4. What output should I show?

---

## 🧪 Exercise: Identify Input, Variables, Processing, and Output

## 📘 Instructions

For each item in the table below:

* Decide whether it represents:

  * **Input**
  * **Variables**
  * **Processing**
  * **Output**

Put an **X** in the column(s) that best describe each item.

> Some items may belong to **more than one column**.

---

## 📊 Table


| Item                                | Input | Variables | Processing | Output |
| ----------------------------------- | ----- | --------- | ---------- | ------ |
| User types their name               |       |           |            |        |
| The number of hours worked          |       |           |            |        |
| The tax rate stored in the program  |       |           |            |        |
| Multiplying hours by pay rate       |       |           |            |        |
| Displaying “Your total is $250”     |       |           |            |        |
| Asking the user for their age       |       |           |            |        |
| The variable `total_price`          |       |           |            |        |
| Converting Fahrenheit to Celsius    |       |           |            |        |
| The result of a calculation         |       |           |            |        |
| Reading a number from the keyboard  |       |           |            |        |
| Adding three test scores together   |       |           |            |        |
| The message “You passed!”           |       |           |            |        |
| A stored value in memory            |       |           |            |        |
| Calculating an average              |       |           |            |        |
| Printing the final answer           |       |           |            |        |
| The value 0.07 stored as `tax_rate` |       |           |            |        |
| Typing a password                   |       |           |            |        |
| A named memory location             |       |           |            |        |
| Showing a receipt on the screen     |       |           |            |        |
| Applying a formula                  |       |           |            |        |

---

# 🧑‍🎓 The Most Important Takeaway

> Programming is not about memorizing syntax.
> It is about **solving problems using input, variables, processing, and output.**

---

# 🧭 Final Truth

> The **ideas** stay the same.
> Only the **language** changes.

---

# 🧰 What Is the `.venv` Folder? (Virtual Environment)

When you create a new Python project in PyCharm, you will notice a folder named:

```
.venv
```

This stands for:

> **Virtual Environment**

---

## 🧠 What Does That Mean?

A **virtual environment** is like a **private copy of Python just for this project**.

Think of it like this:

> Each Python project gets its **own little bubble** so it doesn’t interfere with other projects.

This means:

* ✅ Each project has its **own Python setup**
* ✅ Projects don’t break each other
* ✅ Installing things in one project won’t affect another
* ✅ Your project will work the same way on another computer

---

## 🏠 Real-Life Analogy

Imagine your computer is an **apartment building**:

* The building = your computer
* Each apartment = a Python project
* The `.venv` = everything inside *that apartment*

Each apartment has:

* Its own kitchen
* Its own food
* Its own supplies

But:

* One apartment’s stuff does **not** affect the others.

---

## 🧪 What Is Inside `.venv`?

Inside the `.venv` folder is:

* A copy of Python
* Tools Python needs to run
* Any extra libraries you might install later

> ⚠️ You normally **do not open or edit** this folder.

---

## 🚫 Should I Touch the `.venv` Folder?

**No.**

> PyCharm manages this folder automatically for you.

For this course:

> ✅ You can safely **ignore the `.venv` folder**

---

## 📁 Where Is *My* Code?

Your Python programs are in files like:

```
hello.py
calculator.py
main.py
```

The `.venv` folder just helps Python **run** your code correctly.

---

## 🧨 What If `.venv` Is Deleted?

Nothing bad happens:

* PyCharm will **recreate it automatically**
* Your code files will still be safe

---

## 🧑‍🎓 The Short Version (Remember This)

> “The `.venv` folder is my project’s private Python. I don’t need to touch it. PyCharm uses it behind the scenes.”

---

## 🧠 Why Are We Using This?

Because this is:

* ✅ Professional, real-world practice
* ✅ Prevents problems later
* ✅ Makes projects portable and reliable

But PyCharm **handles all the hard parts for you**.

---

## ✅ For This Class

* Do **not** delete it
* Do **not** edit it
* Do **not** worry about it

Just focus on writing your Python code. 🐍

---

# 🛠️ Part 2: Creating a Python Project in PyCharm

## Instructor Demo:

1. Open PyCharm → New Project → Name it: `IntroPython`
2. Show:

   * Project window
   * Where files go
3. Create file: `first_program.py`

    Type:
    
    ```python
    # Program: First Python Program
    # Author: Your Name
    # Purpose: Demonstrate basic output
    
    print("Hello, world!")
    print("Python is working!")
    ```
4. Right-click → Run

---

## Student Practice:

* Create project `IntroPython`
* Create file `hello.py`
* Add:

  * 2 comment lines at top
  * 2 print statements
* Run it

---

# 📝 Part 3: Comments and Program Design

Explain:

    ```python
    # This is a comment
    ```

Why we use them:

* Explain purpose
* Explain tricky code
* Leave notes for ourselves and others

Show **design-first thinking**:

    ```python
    # 1. Ask user for two numbers
    # 2. Add them
    # 3. Display the result
    ```

---

# 📦 Part 4: Variables, Input, and Output

## Instructor Demo:

Create: `input_demo.py`

    ```python
    # Program: Input Demo
    # Purpose: Show variables and input
    
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    
    print("Hello", name)
    print("Next year you will be", age + 1)
    ```

Explain:

* `input()` always returns **text**
* We convert using:

    ```python
    int()
    float()
    ```

---

# 🧮 Part 5: Calculations

## Instructor Demo:

Create: `math_demo.py`

```python
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = length * width
perimeter = 2 * (length + width)

print("Area:", area)
print("Perimeter:", perimeter)
```

Explain:

* `+ - * /`
* Order of operations
* Parentheses

---

# ⚠️ Common Beginner Errors 

| Problem             | Fix                               |
| ------------------- | --------------------------------- |
| Input used in math  | Convert with `int()` or `float()` |
| Weird string errors | Don’t add strings to numbers      |
| Program won’t run   | Make sure correct file is run     |
| Misspelled variable | Names must match exactly          |

---

# 🧱 Starter Template for Struggling Students

```python
#
# Student Name:
# Date:
# Purpose of Program:
#
```

---


