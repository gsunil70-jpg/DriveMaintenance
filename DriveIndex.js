class DriveIndex {


  constructor() {

    this.files = [];

    this.folders = [];

  }


  addFile(fileRecord) {

    this.files.push(fileRecord);

  }


  addFolder(folderRecord) {

    this.folders.push(folderRecord);

  }


  getFiles() {

    return this.files;

  }


  getFolders() {

    return this.folders;

  }


  getFileCount() {

    return this.files.length;

  }


  getFolderCount() {

    return this.folders.length;

  }


}