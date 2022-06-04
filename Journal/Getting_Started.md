# Getting Started

Selfteach is a web app for helping me learn and practice with technical textbooks. 

This tool has been created by me for personal use numerous times in numerous incarnations. I am taking some time to do it right, and document my process along the way. I am inexperienced in the Javascript/Node world, and so I hope this will be a nice learning exercise. 

## Features

What is the definition of done for the features the app provides?

I have a landing page that looks nice and describes the product

I have a library of books that I am making progress through
    - I can see my progress through any book in fine grained and high level form
    - I can edit the data associated with any book without going into storage, including marking a chapter as "studied" and thus elligible to be used in a problem set
    - I can add books to and remove books from this personal library seamlessly

I can autogenerate problem sets from the books I am studying
    - I can generate a new problem set from uncompleted problems in the textbooks in my library
        Sub-criteria (form):
        - select which books participate
        - specify number of problems
        - Chapter and book are selected randomly (must have already studied), but once that is pinned down, the "next" problem is selected in order
    - I have a list of current problem sets, I can view or edit any of them
    - I can mark individual problems on the problem set as complete
    - I can "complete" a problem set, with the affect that all the problems from the set get marked as complete in the data for the books
    - I can delete a problem set
    - (stretch) I can view the history of completed problem sets, and store the files from my work on the and view those as well

## Engineering Excellence Requirements

Durability

- App is well-tested, and durable to strange user interactions
- App is impossible to break in happy path, and is not easy to break in wrecking ball path

Users, AuthE/AuthZ, protected API, security

- User must login to view and edit his data
- The architecture of the system allows for multiple users
- service handles secrets correctly

DevOps
- I have a defined and enforced git flow which prevents bad code from reaching PROD
- I have a fast automated build pipeline
    - gated on lint, tests, coverage
- I have a reliable, low-cost hosting platform
- Deployments are quick, automated, and easy
- I can easily spin up a local or/and cloud-based test enviroment
- I can easily deploy application infrastructure in an automated way
- Package management makes code dependencies easy

Language/Framework/Tech Stack
- JS - after having written the app so that it just *works*, it is rewritten to be elegant, idiomatic Javascript
- The code is sensibly organized
- Cloud storage is used well in terms of data model and features used for data type. Cost is low and performance is high. 

Style/layout/Design
- Project uses modern styling methods to have be consistent, seamless, and pleasant
- Project has a nice logo that I designed (a fun way to learn some digital design skills)
- Works well on mobile and desktop

TypeScript
- The project is converted from Javascript to Typescript, and this conversion actually provides value to the project