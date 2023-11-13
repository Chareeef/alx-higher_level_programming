#!/usr/bin/node

module.exports.addMeMaybe = (nb, func) => {
  nb++;
  func(nb);
};
