class AuditLogger {

  constructor() {
    this.entries = [];
  }


  log(action, status, message) {

    this.entries.push({

      timestamp: new Date(),

      action: action,

      status: status,

      message: message

    });

  }


  getEntries() {

    return this.entries;

  }


  print() {

    Logger.log(
      JSON.stringify(
        this.entries,
        null,
        2
      )
    );

  }

}
