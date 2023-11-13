#!/usr/bin/node
/* Execute a function n times */
module.exports.callMeMoby = (n, func) => {
  for (let i = 0; i < n; i++) {
    func();
  }
};
