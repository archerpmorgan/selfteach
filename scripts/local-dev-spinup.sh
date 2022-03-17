#!/bin/bash
(cd server && npm install)
(cd server && npm start &)


(cd client && npm install)
(cd client && npm start &)
