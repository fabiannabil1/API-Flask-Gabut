namespace WinFormsApp2
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            qr_box = new PictureBox();
            ((System.ComponentModel.ISupportInitialize)qr_box).BeginInit();
            SuspendLayout();
            // 
            // qr_box
            // 
            qr_box.Location = new Point(10, 12);
            qr_box.Name = "qr_box";
            qr_box.Size = new Size(438, 428);
            qr_box.SizeMode = PictureBoxSizeMode.StretchImage;
            qr_box.TabIndex = 0;
            qr_box.TabStop = false;
            qr_box.Click += qr_box_Click;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(7F, 15F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(460, 450);
            Controls.Add(qr_box);
            Name = "Form1";
            Text = "Form1";
            Load += Form1_Load;
            ((System.ComponentModel.ISupportInitialize)qr_box).EndInit();
            ResumeLayout(false);
        }

        #endregion

        private PictureBox qr_box;
    }
}
