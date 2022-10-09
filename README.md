# for-pre-interview
This repository contains two part: [task_1](task_1)(Data aggregation) and [task_2](task_2)(Simple TODO app).


## task_1
*task_1* is an application, which groups data from given ".csv" file.  
*task_1* consists of two files: *data.csv* and *solution.py*.  
*data.csv* file contains two columns: *country* and *person*.  
App *solution.py* reads data from *data.csv* file and groups this data by the country and 
print out all the people and their count for each country.

#### How to run this application  
For using this application you shlould do the following steps:
1. Clone this repository. It can be done by two ways:  
If you use the web URL:  
`git clone https://github.com/nvkuntsevych/for-pre-interview.git`  
If you use the SSH key:  
`git clone git@github.com:nvkuntsevych/for-pre-interview.git`  
2. Open the *task_1* directory, which is in *for-pre-interview* directory;  
3. Run the *solution.py* file.  

### How to use this application with own *.csv* file  
If you want to use your own *.csv* file for grouping and printing out, you should do the next things:  
1. Insert your *.csv* file into *task_1* directory. *data.csv* file must contain only two columns: *country* and *person*;  
2. Open *solution.py* file and specify name of inserted *.csv* file and path to it with *PATH_TO_FILE* variable;  
3. Run the *solution.py* file.  



## task_2
*task_2* is a simple TODO application.   

#### How to run this application  
For using this application you shlould do the following steps:
1. Clone this repository. It can be done by two ways:  
If you use the web URL:  
`git clone https://github.com/nvkuntsevych/for-pre-interview.git`  
If you use the SSH key:  
`git clone git@github.com:nvkuntsevych/for-pre-interview.git`  
2. Open the *task_2* directory, which is in *for-pre-interview* directory;  
3. Run the *solution.py* file.  

### How to use this application    
This app supports the following commands:  
help - display this information;  
add <your_task> - add new task with description 'your_task'. You can enter multiple tasks separated by a comma;  
remove <task_id> - remove task with id 'task_id'. You can enter multiple tasks ids separated by a comma;  
list - display active tasks;  
mark <task_id> - mark task with id 'task_id' as done;  
statistic - display the number of comleted tasks grouped by date;  
exit - exit this app.  