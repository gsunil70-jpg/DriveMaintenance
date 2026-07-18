/**
 * ============================================================
 * DriveMaintenance v1.1
 * Storage Catalog
 * ============================================================
 * Collection of StorageObject instances.
 */

class StorageCatalog {

  constructor() {

    this.objects = [];

  }


  add(storageObject) {

    this.objects.push(storageObject);

  }


  getAll() {

    return this.objects;

  }


  count() {

    return this.objects.length;

  }


  isEmpty() {

    return this.count() === 0;

  }


  getFiles() {

    return this.objects.filter(function(object) {

      return object.objectType === OBJECT_TYPE.FILE;

    });

  }


  getFolders() {

    return this.objects.filter(function(object) {

      return object.objectType === OBJECT_TYPE.FOLDER;

    });

  }


  insideBackup() {

    return this.objects.filter(function(object) {

      return object.isInBackup;

    });

  }


  outsideBackup() {

    return this.objects.filter(function(object) {

      return !object.isInBackup;

    });

  }


  totalSize() {

    return this.getFiles().reduce(

      function(total, object) {

        return total + object.size;

      },

      0

    );

  }


  largestFile() {

    const files =
      this.getFiles();

    if (files.length === 0) {
      return null;
    }

    return files.reduce(function(largest, current) {

      return current.size > largest.size
        ? current
        : largest;

    });

  }


  clear() {

    this.objects = [];

  }

}