1.jquery.history.js：
    该文件是操作浏览器历史记录的。

2.jquery.pjax.js
	该文件是进行无刷新跳转页面用的。

	/**
	 * 重要说明：
	 * 1.第一个参数是要响应 pjax 的元素。
	 * 2.第二个参数是当前页面要替换成新页面的元素的索引器（如：Id, class 等）。
	 * 3.第三个参数是一个数组，参数看文档：http://www.uedsc.com/jquery-pjax-js.html。
	 *     补充说明：fragment 参数表示，跳转后的页面的哪个容器的内容替换掉当前页面。
	 *
	 * 示例：
	 * 1.现在有两个页面。
	 * 2.当前打开的页面 A 中，在 body 元素下有一个 div，它的 Id 是“pjax-container”。
	 * 3.现在目的是想要无刷新的跳转到 B 页面。
	 * 3.1.由于已经在 A 页面定义了 pjax 的初始化信息：$(document).pjax('a[target!=_blank]', '#pjax-container', { fragment: '#main', timeout: 8000 });。
	 *         表示，将 B 页面中，Id 是“main”的元素替换掉 A 页面中 Id 是“pjax-container”的元素。
	 * 3.2.在 A 页面增加 Id 是“pjax-container”的元素，并将需要替换掉的内容放到该元素里。
	 * 3.3.在 B 页面增加 Id 是“main”的元素，同样将切换后的内容放到该元素里。
	 * 4.完成。
	 * -------------------------------------------------------------------------------------------------
	 */
	$(document).pjax('a[target!=_blank]', '#pjax-container', { fragment: '#main', timeout: 8000 });