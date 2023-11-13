#!/usr/bin/node
const addMaybe = require('./102-add_me_maybe').addMeMaybe;
addMaybe(4, (nb) => {
  console.log('New value:', nb);
});
