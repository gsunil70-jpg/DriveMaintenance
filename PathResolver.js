class PathResolver {


  constructor() {

    this.cache = {};

  }



  getFolderPath(folderId) {


    if (this.cache[folderId]) {

      return this.cache[folderId];

    }


    let path = "";


    let currentId = folderId;


    while (currentId) {


      if (this.cache[currentId]) {

        path =
          this.cache[currentId] + path;

        break;

      }


      const folder =
        DriveApp.getFolderById(currentId);


      const name =
        folder.getName();


      if (name !== "My Drive") {

        path =
          "/" + name + path;

      }


      const parents =
        folder.getParents();


      if (parents.hasNext()) {

        currentId =
          parents.next().getId();

      }

      else {

        currentId = null;

      }

    }


    this.cache[folderId] = path;


    return path;


  }



  getFilePath(file) {


    const parents =
      file.getParents();


    if (!parents.hasNext()) {

      return "/" + file.getName();

    }


    const folder =
      parents.next();


    return (

      this.getFolderPath(folder.getId())

      +

      "/"

      +

      file.getName()

    );


  }



  isInsideBackup(path) {


    return path
      .toLowerCase()
      .startsWith(
        "/backup/"
      );


  }


}