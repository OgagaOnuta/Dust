(global-display-line-numbers-mode)
(electric-pair-mode)

(setq-default indent-tabs-mode nil)
(setq-default tab-width 4)

(setq c-default-style "linux")
(setq c-tab-width 8)
(setq js-tab-width 2)

(defvaralias 'c-basic-offset 'c-tab-width)
(defvaralias 'cperl-indent-level 'tab-width)
(setq-default js-indent-level js-tab-width)

(setq c-backspace-function 'backward-delete-char)

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(ansi-color-faces-vector
   [default default default italic underline success warning error])
 '(ansi-color-names-vector
   ["#242424" "#e5786d" "#95e454" "#cae682" "#8ac6f2" "#333366" "#ccaa8f" "#f6f3e8"])
 '(custom-enabled-themes nil))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
