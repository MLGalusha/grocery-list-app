import AddItem from "./AddItem";
import { ItemType } from "../types";
import Item from "./Item";

interface ItemListProps {
  itemList: ItemType[];
  onModifyItemList: (itemList: ItemType[]) => void;
  onAddItem: (item: ItemType) => void;
}

export default function ItemList({
  itemList,
  onModifyItemList,
  onAddItem,
}: ItemListProps) {
  return (
    <div>
      <AddItem onAddItem={onAddItem} />
      <ul>
        {itemList.map((item) => (
          <Item
            key={item.id}
            item={item}
            itemList={itemList}
            onModifyItemList={onModifyItemList}
          />
        ))}
      </ul>
    </div>
  );
}
