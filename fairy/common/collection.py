# config=utf-8


def get_pager(page_index, page_size, item_count, show_page_count):
    """
        获得分页信息。
    Args:
        page_index: 当前页码。
        page_size: 页大小。
        item_count: 总记录数。
        show_page_count: 显示的页码数。

    Returns:
        分页信息字典。
    """

    # 总页数
    total_page_count = 0

    # 上一页
    prev_page = 0

    # 下一页
    next_page = 0

    # 最小页码
    min_page = 0

    # 最大页码
    max_page = 0

    # 计算总页数。
    if item_count > 0 and page_size > 0:
        total_page_count = int(item_count / page_size)

    # 只显示 100 页
    if total_page_count > 100:
        total_page_count = 100

    # 计算上一页。
    if page_index - 1 > 1:
        prev_page = page_index - 1
    else:
        prev_page = 1

    # 计算下一页。
    if page_index + 1 < total_page_count:
        next_page = page_index + 1
    else:
        next_page = total_page_count

    # 计算最小页码。
    if page_index - show_page_count > 1:
        min_page = page_index - show_page_count
    else:
        min_page = 1

    # 计算最大页码。
    if page_index + show_page_count < total_page_count - 1:
        max_page = page_index + show_page_count
    else:
        max_page = total_page_count

    return dict(
            page_index=page_index,
            page_size=page_size,
            item_count=item_count,
            total_page_count=total_page_count,
            prev_page=prev_page,
            next_page=next_page,
            min_page=min_page,
            max_page=max_page)
