function part1(inp) {
	var pos = 0;
	var o = 0;
	for (var i == 0; i < inp.length; i ++) { //Loop through input
		pos += 1;
		if (pos >= inp.length) {pos -= inp.length;} //Make circular
		if(input.charAt(i) == input.charAt(pos)) {o += parseInt(input.charAt(i));}} //Add number if equal
	return o; //Send back answer to part 1
}
	
function part2(inp) {
	var pos = 0;
	var o = 0;
	for (var i == 0; i < inp.length; i ++) { //Loop through input
		pos = i + inp.length / 2;
		if (pos >= inp.length) {pos -= inp.length;} //Make circular
		if(input.charAt(i) == input.charAt(pos)) {o += parseInt(input.charAt(i));}} //Add number if equal
	return o; //Send back answer to part 2
}

console.log("Part 1: " + part1(1111));
console.log("Part 2: " + part2(1212))
