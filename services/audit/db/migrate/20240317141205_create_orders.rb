class CreateOrders < ActiveRecord::Migration[7.1]
  def change
    create_table :orders do |t|
      t.string :order_id
      t.string :customer_id
      t.string :order_status
      t.decimal :order_total, precision: 10, scale: 2
      t.json :order_items
      t.timestamps
    end
  end
end
