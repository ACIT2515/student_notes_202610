# Exercise: Understanding Recursion with Traceroute Debugger

## Overview

This exercise re-implements a real-world network diagnostic tool: `traceroute`,
in Python to demonstrate recursion. You'll debug the code to see how recursive
calls build up and how base cases terminate the recursion.

---

## Setup: Running VS Code as Administrator

**IMPORTANT:** This program requires administrator/root privileges to create raw
ICMP sockets.

### Windows Instructions

#### Method 1: Run VS Code as Administrator

1. Close VS Code if it's currently running
2. Right-click on the VS Code icon in Start Menu or Desktop
3. Select **"Run as administrator"**
4. Click **"Yes"** when prompted by User Account Control
5. Open your workspace folder
6. Navigate to `demos/recursion/traceroute/traceroute.py`

#### Method 2: Run from Elevated PowerShell

1. Press `Win + X` and select **"Windows PowerShell (Admin)"** or **"Terminal
   (Admin)"**
2. Navigate to VS Code installation directory:
   ```powershell
   cd "C:\Users\YourUsername\AppData\Local\Programs\Microsoft VS Code"
   ```
3. Launch VS Code:
   ```powershell
   .\Code.exe "C:\path\to\your\workspace"
   ```

### Linux/Mac Instructions

```bash
sudo code --user-data-dir="/tmp/vscode-root"
```

**Note:** Running as administrator is only needed when you actually run/debug
the traceroute program. You can edit the code without admin privileges.

---

## Windows Firewall Setup (If Needed)

If you encounter issues with ICMP packets being blocked, run these PowerShell
commands as Administrator:

```powershell
New-NetFirewallRule -DisplayName "Allow ICMPv4 Inbound Ping" -Direction Inbound -Protocol ICMPv4 -IcmpType 8 -Action Allow -Profile Any
```

```powershell
New-NetFirewallRule -DisplayName "Allow ICMPv4 Outbound Ping" -Direction Outbound -Protocol ICMPv4 -Action Allow -Profile Any
```

---

## Part 0: Exisiting Tools: `traceroute` and `network-test`

Before analyzing the Python code, run the standard network diagnostic tools
included with your operating system to understand the basic operation of
`traceroute`.

### Linux / MacOS (`traceroute`)

Open a terminal and use the `traceroute` command followed by a destination:

```bash
traceroute google.com
```

### Windows PowerShell (`Test-NetConnection`)

Open PowerShell as Administrator and run:

```powershell
Test-NetConnection google.com -TraceRoute
```

_(Note: You can also use the classic `tracert google.com` command)_

### Observation Question

**Q0:** Run the command for your OS. Look at the output list.

- Does the millisecond (ms) time generally increase as the hop count gets
  higher?
- Do you see any lines with `*` or `Request Timed Out`? What might this signify
  about that router's configuration regarding ICMP packets?

---

## Part 1: Code Analysis (Before Debugging)

Before you start debugging, read through [traceroute.py](traceroute.py) and
answer these questions:

### Question 1: Identifying Base Cases

Examine the `recursive_traceroute()` function

#### Q1a: How many base cases does this function have? List them.

#### Q1b: What conditions trigger each base case?

#### Q1c: Why is it important to have a maximum hops limit as a base case?

### Question 2: Identifying the Recursive Case

#### Q2a: Where in the code does the recursive call happen? (Provide the line number)

#### Q2b: What parameter changes with each recursive call?

#### Q2c: How does this parameter change move us closer to a base case?

### Question 3: Understanding the Recursion Pattern

#### Q3a: If you trace to a destination that is 5 hops away, how many times will `recursive_traceroute()` be called?

#### Q3b: What would happen if the base cases were removed?

#### Q3c: Why doesn't this function return a value? What does it do instead?

---

## Part 2: Debugging Setup

### Step 1: Set Breakpoints

1. Open [traceroute.py](traceroute.py)

2. Set a breakpoint on line 46 (inside `recursive_traceroute`, right after the
   base case check):

   ```python
   if ttl > max_hops:
   ```

   Click in the gutter to the left of the line number to set the breakpoint.

3. Set another breakpoint on line 111 (the recursive call):
   ```python
   recursive_traceroute(dest_ip, ttl + 1, max_hops, timeout)
   ```

### Step 3: Start Debugging

1. Ensure VS Code is running as administrator
2. Select **"Traceroute Debug** from the debug configuration dropdown
3. Press `F5` to start debugging
4. The debugger will stop at your first breakpoint

---

## Part 3: Debugger Questions

Now debug the program and answer these questions based on what you observe:

### Question 4: First Recursive Call

#### Q4a: When the debugger stops at your first breakpoint, what is the value of `ttl`?

#### Q4b: Look at the **CALL STACK** panel in the debugger. How many function calls are currently on the stack?

#### Q4c: Step through the code until you reach the recursive call. Before the recursive call executes, what will be the value of `ttl` passed to the next call?

### Question 5: Watching the Stack Grow

#### Q5a: After the first recursive call, look at the **CALL STACK** panel again. How has it changed?

#### Q5b: Press `F5` to continue to the next breakpoint. Check the CALL STACK panel. How many `recursive_traceroute` calls are now on the stack?

#### Q5c: In the **VARIABLES** panel, examine the `ttl` variable. Why is it different from the previous iteration?

#### Q5d: Continue pressing `F5` several times. Describe what you observe happening to the call stack.

### Question 6: Reaching a Base Case

#### Q6a: Continue debugging until you reach a base case. Which base case was triggered?

#### Q6b: What happens to the call stack when a base case is reached and the function returns?

#### Q6c: How does the program "know" to stop making recursive calls?

### Question 7: Understanding TTL Behavior

#### Q7a: Set a breakpoint inside the `try` block where the ICMP packet is sent (around line 103). Run the debugger again. What value does TTL start at?

#### Q7b: Each time you continue to the next iteration, increment your counter. At what TTL value does the program stop (assuming you reach the destination)?

#### Q7c: How does incrementing TTL help discover the path to the destination?

### Question 8: Stack Unwinding

#### Q8a: Add a breakpoint on the `return` statement inside the base case (around line 134). When this breakpoint is hit, examine the call stack. How many function calls are waiting to complete?

#### Q8b: Step out of the function (`Shift+F11`). Where does execution continue?

---

## Part 4: Experimentation

### Experiment 1: Change the Destination

Trace a different host: github.com

Does the number of recursive calls change? Why or why not?

### Experiment 2: Test Base Case 1

Use only 2 max hops to a distant destination:

What happens? Which base case is triggered?

### Experiment 3: Observe Timeout

Try tracing to a destination that might have some hops that don't respond:
`8.8.8.8`

Watch the output. What happens when a hop times out? Does the recursion
continue?

---

## Part 5: Reflection Questions

### R1: Compare this recursive implementation to how you might write this using a `for` or `while` loop. What are the advantages and disadvantages of the recursive approach?

### R2: How does the call stack relate to the "path" that traceroute discovers?

---

### Part 6: Reimplementation

Using the `traceroute_accumulate.py` as starter code reimplement the
`recursive_traceroute()` function to return a list of all hops instead of just
printing them. Each hop in the list is a dictionary comprised of a dictionary
with two keys:

- `Node`: the ip address of the node
- `Time`: the return trip time of the echo request

You'll need to:

1. Change the function signature to return a list
2. Build up the list through recursive calls
3. Handle the base cases appropriately

## Troubleshooting

### "Permission denied" or "An attempt was made to access a socket in a way forbidden"

- Make sure VS Code is running as Administrator (Windows) or with sudo
  (Linux/Mac)
- Check Windows Firewall settings

### Debugger doesn't stop at breakpoints

- Ensure your breakpoints are on executable lines (not comments or blank lines)
- Check that `"justMyCode": true` is in your launch configuration

### All hops show "Request timed out"

- Check your internet connection
- Some networks block ICMP packets
- Try a different destination (e.g., `8.8.8.8` - Google's DNS)

### "Cannot resolve hostname" error

- Check the destination spelling
- Ensure you have internet connectivity
- Try using an IP address directly instead of a hostname

---
