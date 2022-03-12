# Day 1

Agenda

- [x] Create repository
- [x] Create README and a 'getting started' file with project description and feature itemization
- [] Create shell project with all the starter files, and be able to run locally and see something
- [] My .gitignore is up and running and is appropriate for my tech stack
- [] I have the Azure resources I need to host the started app
- [] The app is hosted
- [] I have some starter CI/CD pipelines

## creating shell project

The broad tech stack for the service will be Azure Storage (CosmosDB + Azure Blob) and React+Express+Node, so essentially the "ERN" of MERN but with CosmosDB instead of MongoDB. 

### Express API with Node.js

The backed.

> npm init -y

Creates `package.json` file with project metadata

> npm install --save express

Creates `package-lock.json` which keeps track of dependencies, names and versions, and the `node modules` directory, which stores the module code.

Added some boilerplate startup code to index.js, and now it runs.

### React App

The frontend/SPA that utilizes the Express app

Very simple startup

> npx create-react-app client

Under the hood it this tool does a lot. Some things to know: Babel is a JSX transpiler, and Webpack is a bundler.

### .gitignore

The basic node template does the trick for node. We DO NOT version the node modules directory or other runtime stuff.


#### Resources I used for the day

- What exactly is Node?
  - <https://www.freecodecamp.org/news/what-exactly-is-node-js-ae36e97449f5/>
- What is the JS event loop for?
  - <https://www.freecodecamp.org/news/what-exactly-is-node-js-ae36e97449f5/>
- Starter Express server
  - <https://stackabuse.com/building-a-rest-api-with-node-and-express/>
- Starter React project
  - <https://reactjs.org/docs/introducing-jsx.html>
  - <https://medium.com/@agzuniverse/webpack-and-babel-what-are-they-and-how-to-use-them-with-react-5807afc82ca8>

