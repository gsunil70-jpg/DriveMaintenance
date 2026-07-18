class StateManager {


  constructor() {

    this.properties =
      PropertiesService
      .getScriptProperties();

  }


  save(key, value) {

    this.properties.setProperty(
      key,
      JSON.stringify(value)
    );

  }


  get(key) {

    const value =
      this.properties.getProperty(key);


    if (!value) {

      return null;

    }


    return JSON.parse(value);

  }


  clear(key) {

    this.properties.deleteProperty(
      key
    );

  }


}