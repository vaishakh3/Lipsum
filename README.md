# Lipsum

![](https://y.yarn.co/89e0c3fe-0ce7-4c4b-a348-a5a571b7544f_text.gif)


Lipsum for the laziness of finding a better name is a simple quiz management web app. You might call it a broke person's Quizziz or Kahoot. Our aim is to create a simple web app that has capabilities to :
-  Add Questions
-  Add multiple choice options
-  Create Quiz Rooms
-  Conduct Timed Quizes
  


---

## Contributor's Holy Grail!

### 101 - Writing better commits

The following content is taken form a freeCodeCamp article ([refer this link](https://www.freecodecamp.org/news/how-to-write-better-git-commit-messages/))



**Conventional Commits**

Now that we've covered basic commit structure of a good commit message, I'd like to introduce Conventional Commits to help provide some detail on creating solid commit messages.

At D2iQ, we use Conventional Commit which is a great practice among engineering teams. Conventional Commit is a formatting convention that provides a set of rules to formulate a consistent commit message structure like so:

```
<type>[optional scope]: <description>
[optional body]
[optional footer(s)]
```

The commit type can include the following:

    feat – a new feature is introduced with the changes
    fix – a bug fix has occurred
    chore – changes that do not relate to a fix or feature and don't modify src or test files (for example updating dependencies)
    refactor – refactored code that neither fixes a bug nor adds a feature
    docs – updates to documentation such as a the README or other markdown files
    style – changes that do not affect the meaning of the code, likely related to code formatting such as white-space, missing semi-colons, and so on.
    test – including new or correcting previous tests
    perf – performance improvements
    ci – continuous integration related
    build – changes that affect the build system or external dependencies
    revert – reverts a previous commit 

The commit type subject line should be all lowercase with a character limit to encourage succinct descriptions.

The optional commit body should be used to provide further detail that cannot fit within the character limitations of the subject line description.

---
### Commit Message Comparisons

Review the following messages and see how many of the suggested guidelines they check off in each category.

**Good**

    feat: improve performance with lazy load implementation for images
    chore: update npm dependency to latest version
    Fix bug preventing users from submitting the subscribe form
    Update incorrect client phone number within footer body per client request

**Bad**

    fixed bug on landing page
    Changed style
    oops
    I think I fixed it this time?
    empty commit messages

---