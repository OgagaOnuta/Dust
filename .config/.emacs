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
   '("810742445668fef79362f03b0771aaebfb35933116830d4481ffbfd624aaf832"
     "7eeccb31a6eae175d8bc4216756878a4dfc5bda0a7b66c1aae1677c72520a612"
     "e67a2e6c883901fe5b2c4550593774c3ef94d4e2f62194135a31276e6351af12"
     "cc374577dd31d9b66ededc0ee97524424c4bd32acb446c58c4f2482cbd15b91e"
     "619f66fa889683e83d22301ae0da91cb2e3500b3739f0ea1a840fc9b75764d66"
     "b0a9dc51550b720de6f3646e4bb362c53a4047d8391fe9025ffb9c968cf28091"
     "e3a5959bd8bb6a005cd28fe9e2aba4ca44a0621e5d6e45a7a6c7fbbccc6e1b8d"
     "a79d31939a1d71f3957e26fa1303062489ff92d6090288169e9ff96d98265886"
     "4b4c38d3305dd9bd3158d6363177f9592d2184f7887cb0f6a0079b4b81b5e40f"
     "e07c2e0fd770138e48ec7ad6d4baf79ed341a1782e53b02faa0e522c422a174d"
     "53b6cf6ddf5646495baf047aaa3ccce51406c1e22f023f3ecdb81d2915cfe28d"
     "720c6d102f6b262a3f9c10b4ba27d360a98b74050ade57d4f08ad657567884f4"
     "823b31c469cc27304914137a0c132e855fa7eeec1b36e965eb1dd1f88178dd41"
     "3db825aac83408db00cd80121c01a77b4915b55702c1ab2231ed5c985f4919f5"
     "e3c4a13f658e864b9df5416844c3b4e3ea26fe285a3967ed9829091032b7c6db"
     "343bb08bbb80d3329b57032fd50cff2ab06865eb926279b203d4eb069333d013"
     "8629fd4dad6615677d6de1fb17b9a9b7023980b2c8f8e9dd2aac1f3486dabcd6"
     "f4c33fd8f2ea5f1a088e5a9a5ad964bc426804fd5c7e01270db5684dcd9f8e4f"
     "26822807c8965c03d793307458b886636f41472c38d4d9c5e8e23108114ea08d"
     "a04117d31fcccc8b05deed7536e97a9f3966ed3f62908f5ab92f13cbad3ab319"
     "f4413f5fa68d6f4e157a2a43b97f04301df6c3c895be2f6efe10dfd4fa4d1700"
     "3984e8e9f6d6a20407b731fb1aa492795885020e34f8ad49285547d8058b8217"
     "f0d44ab61fbab644f2ca4e06e6f4cafdc6737efb459a69fc4620dc174f5cd5bd"
     "7e9e2161cca1809a18855dc94660e4fb8f9c9a1a7de2832cf8fe725d9171d7d5"
     "b7f8788b0aed68d595de3d4bdc30e66a233de16f395eb727a5fff2cebd860bd1"
     "6b93b9080b54808151cfae28d78be6722b41af93e58e5dc782a48f0ab8b32a4c"
     "f46e2732cde7d8464065d8e28df6659f3ce1edaafb1bc7b6472a0884e30cf15d"
     "373ae2e3058a31671d2cc434717ef0d00f54888eb47edbc1df6bd1bc30343fa4"
     "528a2975d691779ffab94281acb0d0c7904e15c754c9024686c8eafe2807bffd"
     "f95c826faf00749ea4f726cc5157614440f5b35a73d79221699501e36b7b3524"
     "1836b7b8eb53e7b0133cbfd7b04aefd8b84b7136006c306a7f5f7bb63426f20e"
     "21ad1442cd6eae4593ee6bf6fd7cf627b3116b0a2d8d9c325cf1c49fc95cab44"
     "a6f7143c2fec80690933944fc34bf9e5a5bd0dd57ea39075cb9872e116bf66c3"
     "1d514541f953db5cd8a98572e80d351b228318be1691c2d7bc7c114564ca5503"
     "563eb4e8b8e437dd5f19ae18cf6b246dce59ded6396d1149a4e3defa73f874f4"
     default))
 '(ispell-dictionary nil))

(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
