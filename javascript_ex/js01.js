lst = ['a', 'd', 'c'];
for (i = 0; i < lst.length; i++) {
    console.log(i, lst[i]);
}


let enumerate = (array) => {
    return array.map((value, index) => [index, value])
}
let array = ['a', 'b', 'c']
console.log(enumerate(array))

document.getElementsByClassName('EpisodeListList__thumbnail_area--EL1aw')