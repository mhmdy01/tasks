# Tasks
Tasks is simple CLI tool that can be used to manage your TODOs in the terminal.

```
$ python main.py
Usage: main.py [OPTIONS] COMMAND [ARGS]...

  tasks is a CLI for managing your TODOs.

Options:
  --help  Show this message and exit.

Commands:
  add   Add a new task to your TODO list
  do    Mark a task on your TODO list as complete
  show  Filter tasks by status

$ python main.py add learn python
Added "learn python" to your task list.

$ python main.py add build cli apps
Added "build cli apps" to your task list.

$ python main.py show --all
            All Tasks
┏━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ ID ┃ Task           ┃ Completed ┃
┡━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━┩
│ 1  │ learn python   │ False     │
│ 2  │ build cli apps │ False     │
└────┴────────────────┴───────────┘

$ python main.py show --complete
There are no Complete Tasks...

$ python main.py show --incomplete
        Incomplete Tasks
┏━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ ID ┃ Task           ┃ Completed ┃
┡━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━┩
│ 1  │ learn python   │ False     │
│ 2  │ build cli apps │ False     │
└────┴────────────────┴───────────┘

$ python main.py do 1
You have completed the "learn python" task.

$ python main.py show --complete
        Complete Tasks
┏━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ ID ┃ Task         ┃ Completed ┃
┡━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━┩
│ 1  │ learn python │ True      │
└────┴──────────────┴───────────┘

$ python main.py show --incomplete
        Incomplete Tasks
┏━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━┓
┃ ID ┃ Task           ┃ Completed ┃
┡━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━┩
│ 2  │ build cli apps │ False     │
└────┴────────────────┴───────────┘
```
