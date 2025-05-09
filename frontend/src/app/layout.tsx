import type { Metadata } from "next";
import { Playfair_Display } from "next/font/google";
import "./globals.css";

const PlayfairDisplay = Playfair_Display({
  variable: "--font-playfair_display",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: "Codey",
  description: "A very nice AI chatbot",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${PlayfairDisplay.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
