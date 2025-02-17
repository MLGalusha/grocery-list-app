import { ItemType } from "../types";

interface ItemProps {
  item: ItemType;
  itemList: ItemType[];
  onModifyItemList: (itemList: ItemType[]) => void;
}

export default function Item({ item, itemList, onModifyItemList }: ItemProps) {
  return (
    <div>
      <li>{item.text}</li>
    </div>
  );
}
