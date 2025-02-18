








//!CatProcessingFunctions
use include_dir::{include_dir,Dir};
use rand::seq::SliceRandom;
static CAT_DIR:Dir<'_>=include_dir!("$CARGO_MANIFEST_DIR/cats");
///LoadAVectorOfCatPathsFromTheCAT_DIRFolders
fn load_cats()->Vec<String>{
let mut result:Vec<String>=Vec::new();
let glob="*.txt";
for path in CAT_DIR.find(glob).unwrap(){
result.push(path.path().display().to_string());
}
result
}
///PickACatPathFromASliceOfCatPaths
///
///#Arguments
///
///*`options`-AVectorContainingStringPathsToCatfiles
///
///#Returns
///
///OneOfTheStringsIn`options`,RandomlyPicked
fn pick_cat(options:&[String])->String{
let mut rng=rand::thread_rng();
let result=options.choose(&mut rng);
match result{
None=>"Meow".to_string(),
Some(path)=>path.to_string(),
}
}
///LoadDataFromACatfile
///
///# Arguments
///
///`path`-AStringPathToACatfile
///
///# Returns
///
///AStringContainingTheContentsOfTheCatfile
fn load_cat(path:&str)->String{
let file=CAT_DIR.get_file(path).unwrap();
file.contents_utf8().unwrap().to_string()
}

///PrintCatDataToTheScreen
///
///# Arguments
///
///*`cat`-CatData
fn print_cat(cat:&str){
println!("{}",cat);
}
///PrintTheLiteralString
///
///# Arguments
///
///*`literally`-ABoolean,WhetherToPrintTheLiteralStringOrNot
fn print_literal(literally:bool){
if literally{
println!("IAmLITERALLYthisCat:");
}
}
///PrintACertainNumberOfRandomlyPickedCatsWithALiteralString
///
/// # Arguments
///
///*`literally`-ABoolean,WhetherToPrintTheLiteralStringOrNot
///*`count`-HowManyCatsToPrint
pub fn print_cats(literally:bool,count:u16){
let cat_paths=load_cats();
for _ in 0..count{
print_literal(literally);
let cat_path=pick_cat(&cat_paths);
let cat_art=load_cat(&cat_path);
print_cat(&cat_art);
}
}