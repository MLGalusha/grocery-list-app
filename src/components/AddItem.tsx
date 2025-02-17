import { useState } from "react";
import { ItemType } from "../types";

interface AddItemProps {
  onAddItem: (item: ItemType) => void;
}

export default function AddItem({ onAddItem }: AddItemProps) {
  const [itemQuery, setItemQuery] = useState<string>("");

  function handleSubmit(e: React.FormEvent) {
    e.preventDefault();

    if (!itemQuery.trim()) return;

    const newItem = {
      id: crypto.randomUUID(),
      text: itemQuery,
    };

    onAddItem(newItem);
    console.log(newItem);
    setItemQuery("");
  }
  return (
    <form onSubmit={handleSubmit}>
      <input
        className="add-item"
        value={itemQuery}
        type="text"
        placeholder="Add an item..."
        onChange={(e) => setItemQuery(e.target.value)}
      />
    </form>
  );
}
