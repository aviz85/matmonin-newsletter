def select_top_items(ranked_items):
    print("Selecting top 10 items based on ranking...")
    ranked_items.sort(key=lambda x: (2 * x['relevanceForFamilies'] + x['relevanceForSmallBusinesses']), reverse=True)
    top_items = ranked_items[:10]
    print("Selected top 10 items")
    print(top_items)
    return top_items

def select_top_3(final_rankings):
    print("Selecting top 3 items (2 for families, 1 for businesses)...")
    final_rankings.sort(key=lambda x: (2 * x['relevanceForFamilies'] + x['relevanceForSmallBusinesses']), reverse=True)
    family_items = [item for item in final_rankings if item['relevanceForFamilies'] > item['relevanceForSmallBusinesses']]
    business_items = [item for item in final_rankings if item['relevanceForFamilies'] <= item['relevanceForSmallBusinesses']]
    top_3 = family_items[:2] + business_items[:1]
    print("Selected top 3 items")
    return top_3
