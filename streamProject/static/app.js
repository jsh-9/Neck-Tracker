class FileUpload {
    constructor(input) {
        this.input = input
        this.max_length = 1024 * 1024 * 10; // 10 mb
    }

    upload() {
        this.create_progress_bar();
        this.initFileUpload();
    }

initFileUpload() {
    this.file = this.input.files[0];
    this.upload_file(0, null);
}

(function ($) {
    $('#submit').on('click', (event) => {
        event.preventDefault();
        var uploader = new FileUpload(document.querySelector('#fileupload'))
        uploader.upload();
    });
})(jQuery);

create_progress_bar() {
        var progress = `<div class="file-icon">
                            <i class="fa fa-file-o" aria-hidden="true"></i>
                        </div>
                        <div class="file-details">
                            <p class="filename"></p>
                            <small class="textbox"></small>
                            <div class="progress" style="margin-top: 5px;">
                                <div class="progress-bar bg-success" role="progressbar" aria-valuenow="0" aria-valuemin="0" aria-valuemax="100" style="width: 0%">
                                </div>
                            </div>
                        </div>`
        document.getElementById('uploaded_files').innerHTML = progress
    }
