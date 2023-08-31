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
 '(custom-safe-themes
   '("3984e8e9f6d6a20407b731fb1aa492795885020e34f8ad49285547d8058b8217" "f0d44ab61fbab644f2ca4e06e6f4cafdc6737efb459a69fc4620dc174f5cd5bd" "7e9e2161cca1809a18855dc94660e4fb8f9c9a1a7de2832cf8fe725d9171d7d5" "b7f8788b0aed68d595de3d4bdc30e66a233de16f395eb727a5fff2cebd860bd1" "6b93b9080b54808151cfae28d78be6722b41af93e58e5dc782a48f0ab8b32a4c" "f46e2732cde7d8464065d8e28df6659f3ce1edaafb1bc7b6472a0884e30cf15d" "373ae2e3058a31671d2cc434717ef0d00f54888eb47edbc1df6bd1bc30343fa4" "528a2975d691779ffab94281acb0d0c7904e15c754c9024686c8eafe2807bffd" "f95c826faf00749ea4f726cc5157614440f5b35a73d79221699501e36b7b3524" "1836b7b8eb53e7b0133cbfd7b04aefd8b84b7136006c306a7f5f7bb63426f20e" "21ad1442cd6eae4593ee6bf6fd7cf627b3116b0a2d8d9c325cf1c49fc95cab44" "a6f7143c2fec80690933944fc34bf9e5a5bd0dd57ea39075cb9872e116bf66c3" "1d514541f953db5cd8a98572e80d351b228318be1691c2d7bc7c114564ca5503" "563eb4e8b8e437dd5f19ae18cf6b246dce59ded6396d1149a4e3defa73f874f4" default))
 '(ispell-dictionary nil))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
