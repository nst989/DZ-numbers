//Абстрактный класс Человек
abstract class Human {
    String name;
    int age;

    public Human(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public abstract String getGender();
}
//Класс Мужчина
class Man extends Human {
    public Man (String name, int age){
        super(name, age);
    }
    @Override
    public String getGender() {
        return "Мужской";
    }

}

//Класс женщина
class Woman extends Human {
    public Woman (String name, int  age){
        super(name, age);
    }
    @Override
    public String getGender() {
        return "Женский";
    }
}