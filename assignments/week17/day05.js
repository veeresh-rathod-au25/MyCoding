class person{
    constructor(name,age,city){
        this.name = name;
        this.age = age;
        this.city = city;
    }
    knme(){
        return this.name;
    }
}
class employee extends person{

    constructor(name,age,city ){
        super(name,age,city);

    }
    detach(){
        return (this.name, this.age, this.city);
    }
    get nme(){
        return this.name;
    }
    set name(x){
        this.name = x;
        this.time=new Date();
    }
    change(){
        return this.time
    }

}
let admin = new person("Veer",'26',"Blore");
console.log(admin.knme);