#!/usr/bin/node
// Define the function
exports.nbOccurences = function (list, searchElement) {
  // Use reduce to count occurrences
  const occurrences = list.reduce((count, currentElement) => {
    // If current element matches the search element, increment count
    if (currentElement === searchElement) {
      count++;
    }
    return count;
  }, 0);

  // Return the final count
  return occurrences;
};
