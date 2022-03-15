#!/bin/bash
(cd server && npm install)
npm start ./server/.

(cd client && npm install)
npm start ./client/.
