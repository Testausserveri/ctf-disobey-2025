use clap::Parser;
use clap_num::number_range;
mod meow;
///HelperFunctionToValidateTheCommand-LineNumericArgument
fn valid_cat_count(s: &str)->Result<u16,String>{
number_range(s,0,65535)
}
#[derive(Parser)]
#[command(version,about,long_about=None)]
///PrintASCIICatsToYourTerminal
struct Args{
///HowManyCatsToPrint
#[arg(short='c',long="count",default_value_t=1,value_parser=valid_cat_count)]
count:u16,
///AreYouLiterallyThisCat?
#[arg(short='l',long="literally",action)]
literally:bool
}
///PrintsASCIICatsDependingOnCommand-LineParameters
fn main(){
let args=Args::parse();
meow::print_cats(args.literally,args.count);
}