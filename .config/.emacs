(global-display-line-numbers-mode)
(electric-pair-mode)

(setq-default indent-tabs-mode nil)
(setq-default tab-width 4)

(setq c-default-style "linux")
(setq c-tab-width 8)
(defvaralias 'c-basic-offset 'c-tab-width)

(defvaralias 'cperl-indent-level 'tab-width)

(setq js-tab-width 2)
(setq-default js-indent-level js-tab-width)

(setq c-backspace-function 'backward-delete-char)

;; highlight lines exceeding 80 characters and trailing whitespace
(require 'whitespace)
(setq whitespace-style '(face empty lines-tail trailing))
(global-whitespace-mode t)

;; show current column along with the line
(setq column-number-mode t)

(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(custom-enabled-themes '(Dust))
 '(ispell-dictionary nil))

(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
