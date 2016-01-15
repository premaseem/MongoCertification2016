for (x = 0; x < 200; x++) {
var list = db.grades.find({student_id:x,type:"homework"})
print("fetching record " + x + "list size is " + list.size());

if(list){
if (list[0].score > list[1].score){
db.grades.remove(list[1])
}else {
db.grades.remove(list[0])
}
}
}