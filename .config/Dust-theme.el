(deftheme Dust
  "Personalized theme for OgagaOnuta")

(custom-theme-set-faces
 'Dust
 '(font-lock-builtin-face ((t (:foreground "yellow"))))
 '(font-lock-comment-face ((t (:foreground "color-23"))))
 '(font-lock-keyword-face ((t (:foreground "magenta"))))
 '(font-lock-type-face ((t (:foreground "color-22"))))
 '(font-lock-warning-face ((t (:foreground "red"))))
 '(font-lock-constant-face ((t (:foreground "dark orange"))))
 '(font-lock-function-name-face ((((class color) (min-colors 88)
                                   (background light))
                                  (:foreground "Blue1"))
                                 (
                                  ((class color) (min-colors 88)
                                   (background dark))
                                  (:foreground "medium blue"))
                                 (
                                  ((class color) (min-colors 16)
                                   (background light))
                                  (:foreground "Blue"))
                                 (
                                  ((class color) (min-colors 16)
                                   (background dark))
                                  (:foreground "LightSkyBlue"))
                                 (
                                  ((class color) (min-colors 8))
                                  (:weight bold :foreground "blue"))
                                 (t (:weight bold :inverse-video t))))
 '(font-lock-string-face ((t (:foreground "color-27"))))
 '(font-lock-variable-name-face ((t (:foreground "color-72"))))
 '(default ((t (:inherit nil :extend nil :stipple nil
                         :background "black" :foreground "brightblack"
                         :inverse-video nil :box nil :strike-through nil
                         :overline nil :underline nil :slant normal
                         :weight normal :height 1 :width normal
                         :foundry "default" :family "default"))))
 '(minibuffer-prompt ((((background dark)) (:foreground "magenta"))
                      (((type pc)) (:foreground "magenta"))
                      (t (:foreground "medium blue")))))

(provide-theme 'Dust)
