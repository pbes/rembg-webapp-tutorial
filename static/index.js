document.addEventListener('alpine:init', () => {
    Alpine.data('backgroundRemoval', () => ({
        selectedImage: '',
        images: [
            '',
            '/img/bg-001-1920w.png',
            '/img/bg-003-1920w.png',
            '/img/bg-004-1920w.png',
            '/img/bg-005-1920w.png',
            '/img/bg-006-1920w.png',
            '/img/bg-007-1920w.png',
            '/img/bg-008-1920w.png',
            '/img/bg-009-1920w.png'
        ],
        selectImage(image) {
            this.selectedImage = image;
        }
    }));
})