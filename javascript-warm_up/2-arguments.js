#!/usr/bin/node
const args = process.argv.slice(2); // Exclude the first two elements (node and script path)
const argCount = args.length;

if (argCount === 0) {
    console.log("No argument");
} else if (argCount === 1) {
    console.log("Argument found");
} else {
    console.log("Arguments found");
}