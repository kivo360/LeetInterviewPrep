# Task Scheduler

## The Problem (according to leetcode)
Given a char array representing tasks CPU need to do. It contains capital letters A to Z where different letters represent different tasks. Tasks could be done without original order. Each task could be done in one interval. For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means between two same tasks, there must be at least n intervals that CPU are doing different tasks or just be idle.

You need to return the least number of intervals the CPU will take to finish all the given tasks.


# Common Approach (according to Leetcode) Using Sorting

**This is a straight copy of the leetcode's answer. Python is down below**

Before we start off with the solution, we can note that the names of the tasks are irrelevant for obtaining the solution of the given problem. The time taken for the tasks to be finished is only dependent on the number of instances of each task and not on the names of tasks.

The first solution that comes to the mind is to consider the tasks to be executed in the descending order of their number of instances. For every task executed, we can keep a track of the time at which this task was executed in order to consider the impact of cooling time in the future. We can execute all the tasks in the descending order of their number of instances and can keep on updating the number of instances pending for each task as well. After one cycle of the task list is executed, we can again start with the first task(largest count of instances) and keep on continuing the process by inserting idle cycles wherever appropriate by considering the last execution time of the task and the cooling time as well.

But, there is a flaw in the above idea. Consider the case, where say the number of instances of tasks A, B, C, D, E are 6, 1, 1, 1, 1 respectively with n=2(cooling time). If we go by the above method, firstly we give 1 round to each A, B, C, D and E. Now, only 5 instances of A are pending, but each instance will take 3 time units to complete because of cooling time. But a better way to schedule the tasks will be this: A, B, C, A, D, E, ... . In this way, by giving turn to the task A as soon as its cooling time is over, we can save a good number of clock cycles.

From the above example, we are clear with one idea. It is that, the tasks with the currently maximum number of outstanding (pending)instances will contribute to a large number of idle cycles in the future, if not executed with appropriate interleavings with the other tasks. Thus, we need to re-execute such a task as soon as its cooling time is finished.

Thus, based on the above ideas, firstly, we obtain a count of the number of instances of each task in mapmapmap array. Then, we start executing the tasks in the order of descending number of their initial instances. As soon as we execute the first task, we start its cooling timer as well(iii). For every task executed, we update the pending number of instances of the current task. We update the current time, timetimetime, at every instant as well. Now, as soon as the timer, iii's value exceeds the cooling time, as discussed above, we again need to consider the task with the largest number of pending instances. Thus, we again sort the taskstaskstasks array with updated counts of instances and again pick up the tasks in the descending order of their number of instances.

Now, the task picked up first after the sorting, will either be the first task picked up in the last iteration(which will now be picked after its cooling time has been finished) or the task picked will be the one which lies at (n+1)th(n+1)^{th}(n+1)th position in the previous descending taskstaskstasks array. In either of the cases, the cooling time won't cause any conflicts(it has been considered implicitly). Further, the task most critical currently will always be picked up which was the main requirement.

We stop this process, when the pending instances of all the tasks have been reduced to 0. At this moment, timetimetime gives the required result.



## Explaining The Problem To Your Granny (My Explainations)
I'm making the assumption that explaining the question to your grandma will aid you a lot. That's because your granny doesn't understand much about computers.

### Problem -- What are they asking?
* A **task** is in real life something more complex. It's something you work on. It's a string here. Let's just say it's the real task's name.
* You need to wait a few seconds before taking on the next of the same task. We call that `n`.
* You can do other tasks while you're hanging in the wait time for a given task name.
* How many minimal seconds are we working and waiting in total?
  * What's the lowest wait time assuming you're working on everything with some idle




## TLDR Solution.
* We sort the tasks from most occuring to least.
  * We do this, because logic goes that you'll need these to fill in the gap immediately with items we know we'll see again.
* 

## Code - Python

Here's the python version of the code *(with comments)*:

```py
from heapq import heappush, heappop
from collections import Counter


# Task Scheduler - https://leetcode.com/problems/task-scheduler/

class Solution:
    def inverse(self, num):
        return -1 * num

    def leastInterval(self, tasks: List[str], n: int) -> int:
        # What are the inputs here
        #   - tasks - a list of strings the represent information we're processing
        #   - n - the time between tasks of the exact same time. This would leave us room to process other tasks
        # we asking for here?
        #   - We're looking for an int as an output. That's because we're returning a count
        #   - We're looking for the minimum number of intervals that we're going to use for the problem

        # How I think we're going to solve the problem
        # 1. We process the most important tasks often
        #   - That's because we want to process everything quickly, and processing it quickly means processing the most frequent tasks immediately after the cooldown time is over is necessary.
        # 2. Determine my interval
        #   - I want to be able to determine what step I'm at
        # 3. Create a dict of counts since I last processed my task
        



        # Task map to store if we've seen the item before
        task_count = Counter(tasks)
        current_time = 0
        current_heap = []
        
        # Sorting from least to greatest inside of the heap current_heap
        for k,v in task_count.items():
            heappush(current_heap, (self.inverse(v), k)) # Pushes item from least to greatest (hence the negative values)
        


        # Here we're running through the entire heap and processing the sorted tasks
        while current_heap: # We're running until this list runs out because we intend to pop elements from it
            index, temp = 0, []
            while index <= n:
                current_time += 1 # We're counting the interval time here
                if current_heap:
                    timing, taskid = heappop(current_heap)
                    # We're checking to see if it's at the end of the overall count. 
                    # Remember that it was negative at the beginning
                    if timing != -1:

                        temp.append((timing + 1, taskid))
                # Checking to see if we're out of tasks. Exit the inner loop if both are true.
                # This will automatically exit out of the overall tasks 
                if not current_heap and not temp:  
                    break
                else:
                    index += 1
            # Because we transfered all of the items from the heap to temp, we're transferring them back to know if we should continue
            # heap -> If we're not out of tasks -> temp
            # temp -> Because we're not out -> heap
            for item in temp:
                heappush(current_heap, item)
            # We only stop if we're out of tasks 
            # (Constantly checking the current_heap for if it's empty)
        return current_time 
```

This does give the correct answer.


