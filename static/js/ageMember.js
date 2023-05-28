
//|----------------------------------------------|
//|----------Patrón estructural Mixin------------|
//|----------------Funcinalidad: ----------------|
//|------Este patrón nos permite añadir más------|
//|-----funcionalidades a una clase existente----|
//|------sin tener que modificar la clase.-------|
//|----------------------------------------------|
//|-Se añade la funcionalidad de fecha Edad para-|
//|-el miembro logeado, tomando como parametro la|
//|--fecha de nacimiento de la propiedad title---|
//|--del elemento ageMember y restandola con la--|
//|-fecha actual, tambien enviada como instancia-|
//|-------------en el formato debido-------------|
    const mixin = {
        getEdad() {
            return this.Age;
            return this.nowDate;
        }
    };
    class Age {
        constructor(Age = 0, nowDate = 0 ) {
            this.Age = Age;
            this.nowDate = nowDate;
        }
    }
    Object.assign(Age.prototype, mixin);
    ageSetMemb = ageMember.title; 
    dateNow = new Date().getFullYear();
 
    const p1 = new Age(ageSetMemb,dateNow);

    instanceAge = p1, p1.getEdad();

    ageMember.innerHTML = "  Edad: " + (instanceAge.nowDate - instanceAge.Age) + " años";


