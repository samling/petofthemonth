<template>
  <div class="file-upload">
    <div class="file-upload__area">
      <div v-if="!file.isUploaded">
        <input type="file" name="" id="" @change="handleFileChange($event)" />
        <div v-if="errors.length > 0">
          <div
            class="file-upload__error"
            v-for="(error, index) in errors"
            :key="index"
          >
            <span>{{ error }}</span>
          </div>
        </div>
      </div>
      <div v-if="file.isUploaded" class="upload-preview">
        <img :src="file.url" v-if="file.isImage" class="file-image" alt="" />
        <div v-if="!file.isImage" class="file-extension">
          {{ file.fileExtension }}
        </div>
        <span>
          {{ file.name }}{{ file.isImage ? `.${file.fileExtension}` : "" }}
        </span>
      </div>
      <div class="" style="margin-top: 10px">
        <button @click="sendDataToParent">Select File</button>
      </div>
      <div class="">
        <button @click="resetFileInput">Change file</button>
      </div>
    </div>
  </div>
</template>

  <script>
  import { enIE } from 'date-fns/locale';
  import axios from 'axios';
  import { mapActions } from 'vuex';

  export default {
    name: "FileUpload",
    props: {
      maxSize: {
        type: Number,
        default: 5,
        required: true,
      },
      accept: {
        type: String,
        default: "image/*",
      },
      petId: Number
    },
    data() {
      return {
        errors: [],
        isLoading: false,
        uploadReady: true,
        file: {
          name: "",
          size: 0,
          type: "",
          fileExtension: "",
          url: "",
          isImage: false,
          isUploaded: false,
        },
      };
    },
    methods: {
      ...mapActions(['uploadPetImage']),
      handleFileChange(e) {
        this.errors = [];
        // Check if file is selected
        if (e.target.files && e.target.files[0]) {
              // Check if file is valid
          if (this.isFileValid(e.target.files[0])) {
            // Get uploaded file
            const file = e.target.files[0],
              // Get file size
              fileSize = Math.round((file.size / 1024 / 1024) * 100) / 100,
              // Get file extension
              fileExtension = file.name.split(".").pop(),
              // Get file name
              fileName = file.name.split(".").shift(),
              // Check if file is an image
              isImage = ["jpg", "jpeg", "png", "gif"].includes(fileExtension);
            // Print to console
            console.log(fileSize, fileExtension, fileName, isImage);
            // Load the FileReader API
            const reader = new FileReader();
            reader.readAsDataURL(file)
            reader.addEventListener(
              'load',
              () => {
                // Set file data
                this.file = {
                  name: fileName,
                  size: fileSize,
                  type: file.type,
                  fileExtension: fileExtension,
                  isImage: isImage,
                  url: reader.result,
                  isUploaded: true,
                };
              },
              false
            );
          } else {
            console.log("Invalid file");
          }
        }
      },
      isFileSizeValid(fileSize) {
        if (fileSize <= this.maxSize) {
          console.log("File size is valid");
        } else {
            this.errors.push(`File size should be less than ${this.maxSize} MB`);
        }
      },
      isFileTypeValid(fileExtension) {
        console.log(this.accept.split(","));
        console.log(fileExtension)
        if (this.accept.split(",").includes(fileExtension)) {
          console.log("File type is valid");
        } else {
          this.errors.push(`File type should be ${this.accept}`);
        }
      },
      isFileValid(file) {
        this.isFileSizeValid(Math.round((file.size / 1024 / 1024) * 100) / 100);
        this.isFileTypeValid(file.name.split(".").pop());
        if (this.errors.length === 0) {
          return true;
        } else {
          return false;
        }
      },
      resetFileInput() {
        this.uploadReady = false;
        this.$nextTick(() => {
          this.uploadReady = true;
          this.file = {
            name: "",
            size: 0,
            type: "",
            data: "",
            fileExtention: "",
            url: "",
            isImage: false,
            isUploaded: false,
          };
        });
      },
      async sendDataToParent() {
        this.resetFileInput();
        this.$emit("file-uploaded", this.file);
        try {
          let pet = {
            id: parseInt(this.petId)
          }
          await this.uploadPetImage(pet, this.file)
        } catch (error) {
          console.log(error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
  .file-upload {
  height: 100vh;
  width: 100%;
  display: flex;
  align-items: flex-start;
  justify-content: center;
  }
  .file-upload .file-upload__area {
    width: 600px;
    min-height: 200px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 2px dashed #ccc;
    margin-top: 40px;
  }
  .file-upload .file-upload__error {
    margin-top: 10px;
    color: #f00;
    font-size: 12px;
  }
  .file-upload .upload-preview {
    text-align: center;
  }
  .file-upload .upload-preview .file-image {
    width: 100%;
    height: 300px;
    object-fit: contain;
  }
  .file-upload .upload-preview .file-extension {
    height: 100px;
    width: 100px;
    border-radius: 8px;
    background: #ccc;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0.5em auto;
    font-size: 1.2em;
    padding: 1em;
    text-transform: uppercase;
    font-weight: 500;
  }
  .file-upload .upload-preview .file-name {
    font-size: 1.2em;
    font-weight: 500;
    color: #000;
    opacity: 0.5;
  }
  </style>
  