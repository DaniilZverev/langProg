class SortDictionary {
    let dictionary : [Int : String]
    
    init(dictionary : [Int : String]){
        self.dictionary = dictionary
    }
    
    func sortByKeys(operatorType : String, number : Int){

        switch operatorType{
        case ">":
            for (index, value) in dictionary.sorted(by: {$0.value < $1.value} ){
                if (index > number){
                    print("\(index)=\(value)")
                }
            }
        case ">=":
            for (index, value) in dictionary.sorted(by: {$0.value < $1.value} ){
                if (index >= number){
                    print("\(index)=\(value)")
                }
            }
        case "<":
            for (index, value) in dictionary.sorted(by: {$0.value > $1.value} ){
                if (index < number){
                    print("\(index)=\(value)")
                }
            }
        case "<=":
            for (index, value) in dictionary.sorted(by: {$0.value > $1.value} ){
                if (index <= number){
                    print("\(index)=\(value)")
                }
            }
        default:
            for (index, value) in dictionary.sorted(by: {$0.value < $1.value} ){
                print("\(index)=\(value)")
            }
        }
    }
    
    func sortByKeysIn(firstOperator : String, firstNumber : Int, secondOperator : String, secondNumber : Int){
        if (firstOperator == ">" && secondOperator == "<"){
            for (index, value) in dictionary.sorted(by: {$0.value > $1.value}).reversed(){
                if (index > firstNumber && index < secondNumber){
                    print("\(index)=\(value)")
                }
            }
        }else if(firstOperator == "<" && secondOperator == ">"){
            for (index, value) in dictionary.sorted(by: {$0.value > $1.value}).reversed(){
                if (index < firstNumber && index > secondNumber){
                    print("\(index)=\(value)")
                }
            }
        }else if(firstOperator == "<=" && secondOperator == ">="){
            for (index, value) in dictionary.sorted(by: {$0.value > $1.value}).reversed(){
                if (index <= firstNumber && index >= secondNumber){
                    print("\(index)=\(value)")
                }
            }
        }else if(firstOperator == ">=" && secondOperator == "<="){
            for (index, value) in dictionary.sorted(by: {$0.value > $1.value}).reversed(){
                if (index >= firstNumber && index <= secondNumber){
                    print("\(index)=\(value)")
                }
            }
        }else if(firstOperator == ">" && secondOperator == "<="){
            for (index, value) in dictionary.sorted(by: {$0.value > $1.value}).reversed(){
                if (index > firstNumber && index <= secondNumber){
                    print("\(index)=\(value)")
                }
            }
        }else if(firstOperator == ">=" && secondOperator == "<"){
            for (index, value) in dictionary.sorted(by: {$0.value > $1.value}).reversed(){
                if (index >= firstNumber && index < secondNumber){
                    print("\(index)=\(value)")
                }
            }
        }else if(firstOperator == "<=" && secondOperator == ">"){
            for (index, value) in dictionary.sorted(by: {$0.value > $1.value}).reversed(){
                if (index <= firstNumber && index > secondNumber){
                    print("\(index)=\(value)")
                }
            }
        }else if(firstOperator == "<" && secondOperator == ">="){
            for (index, value) in dictionary.sorted(by: {$0.value > $1.value}).reversed(){
                if (index < firstNumber && index >= secondNumber){
                    print("\(index)=\(value)")
                }
            }
        }
        
    }
    
}

var dict = [1 : "100", 2 : "200", 3 : "300", 4 : "400", 5 : "500", 6 : "600", 7 : "700", 8 : "800", 9 : "900", 10 : "1000", 11 : "1100", 12 : "1200"]

var myDict = SortDictionary(dictionary: dict)
// Обычная сортировка
myDict.sortByKeys(operatorType: ">", number: 5)
print("")
//Сортировка по диапазону
myDict.sortByKeysIn(firstOperator: ">", firstNumber: 5, secondOperator: "<", secondNumber: 8)
