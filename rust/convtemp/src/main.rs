use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() != 3 {
        eprintln!("Invalid number of arguments");
        user_help();
        return
    }

    let temp: i32 = args[2].parse().unwrap();

    match args[1].to_lowercase().as_str() {
        "f" | "fahrenheit" => f_to_c(temp),
        "c" | "celsius" => c_to_f(temp),
        _ => { 
            eprintln!("Invalid tempurature scale specified!");
            return;
        }
    }

}

fn c_to_f (celsius: i32) {
    let ftemp: f64 = (celsius as f64 * 1.8) + 32.0;
    println!("{}c is {:.1}f", celsius, ftemp);

}

fn f_to_c (fahrenheit: i32) {
    let conv_ratio: f64 = 5.0 / 9.0;
    let ctemp = (fahrenheit as f64 - 32.0) * conv_ratio;
    println!("{}f is {:.1}c", fahrenheit, ctemp);

}

fn user_help () {
    println!("Usage:");
    println!("convempt {{f|c|fahrenheit|celsius}} <temp>");
}
