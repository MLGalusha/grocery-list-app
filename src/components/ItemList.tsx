import AddItem from "./AddItem";
import { Item } from "../types";

interface ItemListProps {
  itemList: Item[];
  onModifyItemList: (itemList: Item[]) => void;
  onAddItem: (item: Item) => void;
}

export default function ItemList({
  itemList,
  onModifyItemList,
  onAddItem,
}: ItemListProps) {
  return (
    <div>
      <AddItem onAddItem={onAddItem} />
    </div>
  );
}
