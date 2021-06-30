# Experts Tool

## Setup

Make sure you have virtualenv installed. Run the following commands

```
$ virtualenv venv
$ . venv/bin/activate
$ pip install --editable .
```

Next clone the go repo into the directory

```
git clone https://github.com/golang/go.git
```

To run the expert tool

```
experts [directory] [email]
```

## How it Works

The tool makes use of os.walk to recursively traverse the tree of the directory chosen. The scoring function I created checks for number of lines written using git blame. For each file in the directory we run git blame and check how many lines the email inputed wrote. That is then dived by the total lines of the file to generate a score which represents what percentage of the file that user has written. The scores for all files in the directory are then averaged to give a total contributor score for the directory.

## Future Considerations

The clearest improvement would be to get scores for all users that contributed to the directory which can be done in a single pass of all the files. Second would be the ability to implement multiple features during a single pass (number of commits, first commit, etc.). Third, Some features carry more weight than others. For example if a user has the most commits in a directory, but fewer lines in the current version of the file. We may want to weigh the fact that they've done more commits higher than the lines they written and vice versa.
